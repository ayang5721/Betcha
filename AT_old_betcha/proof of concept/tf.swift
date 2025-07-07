import Foundation
import FoundationNetworking

let input = readLine() ?? ""

let json: [String: String] = ["input": input]
let jsonData = try! JSONSerialization.data(withJSONObject: json)

var request = URLRequest(url: URL(string: "http://127.0.0.1:5000/hash")!)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = jsonData

let task = URLSession.shared.dataTask(with: request) { data, _, error in
    guard let data = data, error == nil else {
        print("Error:", error ?? "Unknown error")
        return
    }

    struct HashResponse: Codable {
        let hash: String
    }

    if let response = try? JSONDecoder().decode(HashResponse.self, from: data) {
        print("SHA256 Hash:", response.hash)
    } else {
        print("Could not parse hash.")
    }
}

task.resume()
RunLoop.main.run()
