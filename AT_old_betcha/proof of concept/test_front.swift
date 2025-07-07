//import SwiftUI

struct ContentView: View {
    @State private var inputText = ""
    @State private var hashed_text = ""

    var body: some View {
        VStack(spacing: 20) {
            TextField( "Enter text to hash", text: $inputText)
                .padding()
                .textFieldStyle(RoundedBorderTextFieldStyle())

        Button("Hash Text") {
            hashInput()
        }

        Text("SHA256 Hash: \(hashed_text)")
            .padding()
            .font(.headline)
            .lineLimit(nil)
        }
        .padding()
    }

    func hashInput() {
        guard let url = URL(string: "http://1270.0.0.1:5000/hash") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let json: [String: String] = ["text": inputText]
        let jsonData = try? JSONSerialization.data(withJSONObject: json)

        request.httpBody = jsonData

        URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else {return}
            if let response = try? JSONDecoder().decode(HashResponse.self, from: data) {
                DispatchQueue.main.async {
                    self.hashed_text = response.hash
                }
            }
        }.resume()
          
    }

}

struct HashResponse: Codable {
    let hash: String
}