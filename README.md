# 📌 URI Parser with Streamlit

## 📖 Description
This is a simple web application built with **Streamlit** to parse and extract components from a **Uniform Resource Identifier (URI)** using **regular expressions (Regex)**. The application automatically detects missing ports and assigns the default port based on the scheme (protocol).

## 👨‍🎓 Assignment Information
**Course:** Semantic Web

**Name:** Alif Al Husaini  
**NPM:** 140810220036  
**Padjadjaran University**

## 🛠 Features
✅ Parses **URI components** (scheme, user info, host, port, path, query, fragment)  
✅ **Auto-assigns default port** if missing (e.g., `http → 80`, `https → 443`)  
✅ **Displays extracted URI components in separate fields**  
✅ **Shows user identity in the sidebar**  
✅ **Interactive web interface** built with **Streamlit**  

### 🌐 Live Demo
Try the deployed version of this app:
[🔗 URI Parser Live](https://uri-parser.streamlit.app/)

## 📌 Installation & Usage
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install Streamlit:
```sh
pip install streamlit
```

### 2️⃣ Clone or Download the Project
```sh
git clone https://github.com/alif-09/TugasSemweb2_URIParser
```

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

### 4️⃣ Open in Browser
Once the command runs, the app will open in your default browser at:
```
http://localhost:8501
```

## 🖥️ Project Structure
```
📁 uri-parser
│── 📄 app.py          # Streamlit web application
│── 📄 uri_parser.py   # Logic to parse URI using Regex
│── 📄 README.md       # Project documentation
```

## 🔎 Example Input & Output
### Input URI:
```
https://user:password@example.com:8080/docs/resource.txt?name=value#section1
```

### Output:
| Field       | Value                           |
|------------|---------------------------------|
| **Scheme**  | `https`                         |
| **User Info** | `user:password`               |
| **Host**    | `example.com`                   |
| **Port**    | `8080`                          |
| **Path**    | `/docs/resource.txt`            |
| **Query**   | `name=value`                    |
| **Fragment** | `section1`                     |

 

## 📜 License
This project is for educational purposes. Feel free to modify and use it as needed.  

---
### 📩 Contact
For any inquiries, feel free to reach out via email: [alhusainialif@gmail.com]  

🚀 **Happy Coding!**
