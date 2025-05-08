import Foundation
import FoundationNetworking

print("Test started")

let url = URL(string: "http://example.com")!
var request = URLRequest(url: url)
request.httpMethod = "GET"

let task = URLSession.shared.dataTask(with: request) { data, _, error in
    if let error = error {
        print("Error:", error.localizedDescription)
    } else {
        print("Networking works.")
    }
}
task.resume()

RunLoop.main.run()
