# Flask Server Setup Guide for Windows, Mac, and Raspberry Pi

This guide provides step-by-step instructions to set up Git, Docker, and run a Flask web server that communicates with a Raspberry Pi.

---

## 🍎 **Mac Setup**

### **1. Install Homebrew**

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### **2. Install Git**

```sh
brew install git
```

### **3. Install Docker Desktop**

```sh
brew install --cask docker
```

- Open Docker Desktop after installation
- Follow the setup wizard
- Ensure Docker Desktop is running (check menu bar icon)

---

## **Windows Setup**

### **1. Install Git**

1. Download Git from [git-scm.com](https://git-scm.com/download/windows)
2. Run the installer with default options
3. Verify installation:
   ```sh
   git --version
   ```

### **2. Install Docker Desktop**

1. Enable WSL2 (Windows Subsystem for Linux):
   ```sh
   wsl --install
   ```
2. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
3. Run the installer
4. Start Docker Desktop
5. Verify installation:
   ```sh
   docker --version
   ```

---

## 🔑 **Git Configuration (All Platforms)**

### **Generate SSH Key for GitHub**

```sh
ssh-keygen -t ed25519 -C "your_personal_email@example.com"
```

### **Copy SSH Key to GitHub**

Mac/Linux:

```sh
cat ~/.ssh/id_ed25519.pub
```

Windows:

```sh
type %USERPROFILE%\.ssh\id_ed25519.pub
```

1. Go to **GitHub → Settings → SSH and GPG Keys**
2. Click **New SSH Key**
3. **Title:** Your device name
4. **Key type:** Authentication Key
5. Paste the key and click **Add SSH Key**

### **Configure Git**

```sh
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---

## 📁 **Project Setup**

### **1. Clone the Repository**

```sh
git clone git@github.com:seintun/proj_web_server.git
cd proj_web_server
```

### **2. Configure Raspberry Pi Connection**

#### Find Raspberry Pi's IP Address

On your Raspberry Pi, run:

```sh
hostname -I
```

This will display the IP address (e.g., 192.168.1.100)

#### Update the IP in Code

1. Open `app.py` in your editor
2. Locate and update the IP:

```python
RASPBERRY_PI_IP = "192.168.1.100"  # Replace with your Pi's actual IP
```

Test the connection in terminal:

```sh
curl http://192.168.1.100:5001/action
```

Expected Response:

```json
{ "message": "Action executed on Raspberry Pi!" }
```

**Important Notes:**

- The IP address may change if your network configuration changes
- For a stable setup, consider setting a static IP on your Raspberry Pi

### **3. Build Docker Image**

```sh
docker build -t flask-web-server .
```

### **4. Run Flask Server**

```sh
docker run -d -p 5005:5005 --name flask-web-server flask-web-server
```

---

## 🔍 **Testing**

### **1. Check Docker Container**

```sh
docker ps
```

### **2. Test Web Interface**

Open in your browser:

```
http://localhost:5005
```

### **3. Click the Button**

This will send a request to the Flask server, which will then communicate with the Raspberry Pi /action endpoint.

Expected response:

```json
{ "status": "success", "response": "Action executed on Raspberry Pi!" }
```

---

## ♻️ **Maintenance Commands**

### **Stop Container**

```sh
docker stop flask-web-server
```

### **Restart Container**

```sh
docker restart flask-web-server
```

### **Remove Container**

```sh
docker rm flask-web-server
```

### **Auto-Restart on Boot**

```sh
docker update --restart unless-stopped flask-web-server
```

### **Remove Docker Resources**

Remove everything (containers, images, networks, and volumes):

```sh
docker system prune -a --volumes -f
```

---

## ✅ **Verification Checklist**

✅ Git installed and configured  
✅ Docker Desktop running  
✅ Repository cloned  
✅ Raspberry Pi IP configured  
✅ Docker container running  
✅ Web interface accessible  
✅ API endpoint responding

---

🚀 **Your local machine is now running a Flask API inside Docker!** 🎯  
For any issues, open a GitHub issue or contact me.  
Happy Coding! 🔦💪
