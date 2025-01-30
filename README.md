# Vulnerable Login Form Demonstration with Flask

This project demonstrates a Regular Expression Denial of Service (ReDoS) vulnerability in a Flask web application.
The login form contains an insecure regular expression that allows an attacker to send specially crafted input, causing excessive resource consumption.

## Features
- ReDoS Vulnerability: The application uses a poorly designed regex (^(a+)+b$) that can be exploited to slow down or crash the server.
- No Security Measures: No account lockout mechanism or rate limiting, making it susceptible to brute-force and DoS attacks.
- No Input Sanitization: The username validation does not properly filter malicious inputs, making it prone to attacks.
- No Authentication System: The app simply checks for a hardcoded password (securepassword), allowing unauthorized access if leaked.

## Prerequisites
- Docker: Install Docker on your machine.
- Python 3.8+ (optional, if running outside Docker).

## Installation & Deployment
1. Clone the Repository
   ```bash
   git clone https://github.com/abarah/ReDos_vul.git
   cd ReDos_vul
   ```
2. Build the Docker Image
   ```bash
   docker build -t flask-vulnerable-login .
   ```
3. Run the Docker Container
   ```bash
   docker run -d -p 5000:5000 flask-vulnerable-login
   ```
4. The application will now be accessible at:
   ```bash
   http://127.0.0.1:5000
   ```

## Exploiting the Vulnerability
1. Triggering a ReDoS Attack
The regular expression ^(a+)+b$ can be exploited using a long sequence of "aaaaaaaaaaaaaaaaaaaaaaaa!" to cause excessive backtracking.
 ```bash
   curl -X POST -d "username=aaaaaaaaaaaaaaaaaaaaaaaa!&password=securepassword" http://127.0.0.1:5000
   ```
The server will slow down significantly or even crash!

## Risks & Mitigations
❌ Denial of Service (DoS): Attackers can send large input strings to freeze the server.
🔐 Mitigation: Use a more secure regex pattern and limit input length.

❌ Brute Force Attacks: No account lockout or rate limiting.
🔐 Mitigation: Implement proper authentication (e.g., hashed passwords, login attempts monitoring).

❌ Hardcoded Passwords: Easily guessed or exposed in source code.
🔐 Mitigation: Store credentials securely using hashing mechanisms like bcrypt.

   

