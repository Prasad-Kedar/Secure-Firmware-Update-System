# Secure-Firmware-Update-System

Enterprise-grade Secure Firmware Update System using FastAPI, React, SQLite, RSA Digital Signatures and JWT Authentication.

## Project Overview

The Secure Firmware Update System is designed to provide a secure Over-the-Air (OTA) firmware update process for IoT and edge devices. It uses RSA digital signatures and SHA-256 hashing to verify the authenticity and integrity of firmware before installation. The project also integrates an automated CI/CD pipeline for secure firmware signing and edge-device verification to prevent unauthorized or tampered firmware updates.

## Features

- Secure Over-the-Air (OTA) firmware updates
- RSA digital signature for firmware authentication
- SHA-256 hash verification for integrity checking
- Automated firmware signing using GitHub Actions
- Edge device signature verification before installation
- Detection of tampered or unauthorized firmware
- Firmware version control to prevent rollback attacks
- REST API support with Swagger documentation
  
 ## Technology Stack

- **Programming Language:** Python
- **Framework:** FastAPI
- **Cryptography:** RSA, SHA-256
- **CI/CD:** GitHub Actions
- **API Documentation:** Swagger UI
- **Version Control:** Git & GitHub
