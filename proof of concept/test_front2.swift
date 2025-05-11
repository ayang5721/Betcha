import Foundation
import FoundationNetworking

struct HashResponse: Codable {
    let hash: String
}

func sendHashRequest(for input: String) {
    let json: [String: String] = ["input": input]
    guard let jsonData = try? JSONSerialization.data(withJSONObject: json) else {
        print("Failed to encode JSON")
        return
    }

    var request = URLRequest(url: URL(string: "http://127.0.0.1:5000/hash")!)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)

    let task = URLSession.shared.dataTask(with: request) { data, _, error in
        defer { semaphore.signal() }

        guard let data = data, error == nil else {
            print("Error:", error ?? "Unknown error")
            return
        }

        if let response = try? JSONDecoder().decode(HashResponse.self, from: data) {
            print("SHA256 Hash:", response.hash)
        } else {
            print("Could not parse hash.")
        }
    }

    task.resume()
    semaphore.wait()
}

print("Enter text to hash (type 'exit' to quit):")

while true {
    print("> ", terminator: "")
    guard let input = readLine()?.trimmingCharacters(in: .whitespacesAndNewlines) else {
        continue
    }
    
    if input.lowercased() == "exit" {
        print("Exiting...")
        break
    }

    sendHashRequest(for: input)
}
