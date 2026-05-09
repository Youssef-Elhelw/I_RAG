# **Basics**
## `You Should know the answers of these questions below Before we start`
## Questions:
### 1. [What is an API and how does HTTP work?](#1-what-is-an-api-and-how-does-http-work-1)?
### __1.1 [What is an API?](#11-what-is-an-api)
### __1.2 [What is a HTTP?](#12-what-is-a-http)
### __1.3 [How HTTP Works (The Request-Response Model)](#13-how-http-works-the-request-response-model)
### __1.4 [What is the Relation between API and HTTP?](#14-what-is-the-relation-between-api-and-http)
### 2. [What is JSON and how do I read/write it?](#2what-is-json-and-how-do-i-readwrite-it)
### __2.1 [Json Key Characteristics](#21-key-characteristics)
### __2.2 [How do i write/read JSON?](#22-how-do-i-writeread-json)
### 3. [What is an API key?](#3-what-is-an-api-key-1)
### 4. [What are HTTP headers and why do APIs need them?](#4-what-are-http-headers-and-why-do-apis-need-them-1)

---

## **1. What is an API and how does HTTP work?**

### 1.1 What is an API?: 
- API stands for Application Programming Interface. In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses.
- In other words: it's a set of rules that allows two software programs to "talk" to each other
<div align="center">
<img src="../Screenshots\API.png" width=700>
</div>

<p style="text-align:center;">────────────</p>

### 1.2 What is a HTTP?
- HTTP (Hypertext Transfer Protocol) is the "language" or protocol these Web APIs use to send and receive that data.

### 1.3 How HTTP Works (The Request-Response Model)
1. **The Request**: The client sends a message containing:
    - Method (Verb): 
        - What the client wants to do (e.g., GET to read data, POST to create it).
            - GET: Retrieve information (like viewing a tweet).
            - POST: Send new information (like posting a new tweet).
            - PUT: Update existing information (like editing a profile).
            - DELETE: Remove information (like deleting a post).
    - Endpoint (URL): 
        - The specific address for the resource.
    - Headers:
        - Extra info like the data format (JSON) or security tokens.
    - Body:
        - Optional data being sent (e.g., your username when logging in).
2. **The Response**: 
    - The server processes the request and sends back:
        - Status Code: A three-digit number showing if it worked (e.g., <span style="color:green">200</span> OK for success, <span style="color:red">404</span> Not Found if the page is missing).
        - Body: The actual content, often formatted as JSON so it's easy for the app to read.

### 1.4 What is the Relation between API and HTTP?

Most modern web APIs are:

- HTTP APIs (REST APIs)

Meaning:

the API rules are implemented
using HTTP requests/responses

So when your app talks to a server:

- Your app sends an HTTP request
- The server's API receives it
- The API processes it
- Server returns an HTTP response

<div align="center">
<img src="../Screenshots\Request_Response.png" width=700>
</div>

<p style="text-align:center;">────────────</p>

--- 

## **2.What is JSON and how do I read/write it?**
- JSON stands for JavaScript Object Notation.
- It is a lightweight format used to store and exchange data between programs, APIs, web apps, and files.
-  It is easy for humans to read and write, and easy for machines to parse and generate

```json
{
    "name": "Youssef",
    "age": 21,
    "skills": ["Python", "C++", "Machine Learning"],
    "is_student": true
}
```

<p style="text-align:center;">────────────</p>

### 2.1 Key Characteristics
- Text-Only: JSON is just a text file, typically saved with a .json extension.Language 
- Independent: While derived from JavaScript, JSON is supported by almost all modern programming languages, including Python, Java, and C++.
- Structure: JSON represents data as key-value pairs (objects) and ordered lists (arrays).
- Data Types: Supported types include strings, numbers, booleans (true/false), null, arrays, and nested objects.

<p style="text-align:center;">────────────</p>

### 2.2 How do i write/read JSON?

- You can see a simple code [here](json_example.py)

---

## **3. What is an API key?**

- An API key is a secret string used to identify and authenticate your application when it communicates with an [API](#11-what-is-an-api).

- When you use services like:

    - OpenAI
    - TMDB
    - Google Maps
    - Hugging Face

- they give you an API key so the server knows:

    - who is making the request
    - usage limits/billing
    - permissions/access rights

<p style="text-align:center;">────────────</p>

- Why API keys are important

    - Think of an API key like:

        - a password for your app
        - or a hotel room key

    - If someone steals it, they may:

        - use your quota
        - cost you money
        - access your data/services

So you should **NEVER** expose it publicly.

<div align="center">
<img src="../Screenshots\API KEY.png" width=700>
</div>

---

## 4. What are HTTP headers and why do APIs need them?

- HTTP headers are extra pieces of information sent along with an HTTP request or response.
- They help the client (like your app/browser) and the server/API communicate properly.

- Why APIs Need Them
    - APIs rely on headers to manage communication without cluttering the actual message body. They are critical for:
        1. **Security & Authentication**: Headers like Authorization carry tokens or API keys to prove a user's identity.
        2. **Content Negotiation**: They tell the server what data format the client expects (e.g., Accept: application/json) and what format is actually being sent (e.g., Content-Type: application/xml).
        3. **Performance: Headers** like Cache-Control instruct browsers or intermediate servers to store data locally, reducing redundant requests.
        4. **Status & Context**: They provide details about the server, the client's software version (User-Agent), or the length of the data being sent (Content-Length).

<p style="text-align:center;">────────────</p>

- Common HTTP Headers in APIsHeader

| Header Name   | Type  (Request/Response)   | Purpose |
|----------------|----------|----------|
| Authorization | Request  | Passes credentials (like a Bearer token) for access. |
| Content-Type  | Both     | Defines the media type (JSON, XML, HTML) of the data body. |
| Accept        | Request  | Specifies what data formats the client can understand. |
| Cache-Control | Both     | Defines how long a response should be cached. |
| User-Agent    | Request  | Identifies the client application or browser making the request. |
| Set-Cookie    | Response | Sends a session ID from the server to the client. |

<p style="text-align:center;">────────────</p>

- Example API Request

``` GET /users HTTP/1.1
Host: api.example.com
Authorization: Bearer abc123
Content-Type: application/json
Accept: application/json 
```
