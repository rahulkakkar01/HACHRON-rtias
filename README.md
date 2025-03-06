# **📦 Real-Time Inventory Auditing System**  

## **📌 Overview**  
The **Real-Time Inventory Auditing System** is designed to **automate inventory management** by continuously tracking stock levels, reducing the need for manual stock-taking, and improving accuracy in warehouse or store inventory.  

It includes:  
- **A dashboard** to monitor inventory in real-time.  
- **Automated data processing** using a CSV dataset (`blinkit.csv`).  
- **Stock insights & visualizations** to help in decision-making.  
- **Warehouse selection** to manage inventory across multiple locations.  

This project is **ideal for businesses, warehouses, and retail stores** looking to improve their **inventory auditing efficiency**.  

---

## **🎯 Features**  
✅ **Dynamic Inventory Dashboard** – Monitor real-time stock levels.  
✅ **Automated CSV-Based Inventory Auditing** – Uses `blinkit.csv` to load and analyze inventory.  
✅ **Real-Time Warehouse Selection** – Track stock across different warehouses.  
✅ **Stock Insights & Graphs** – Visualize demand trends, price-to-demand ratio, and category breakdown.  
✅ **Easy to Use** – Simple web-based interface with modern UI design.  

---

## **🛠 Tech Stack**  
| Component  | Technology Used  |  
|------------|----------------|  
| **Frontend** | HTML, CSS, JavaScript |  
| **Styling & UI** | FontAwesome, Tailwind CSS (if added) |  
| **Backend (Future Scope)** | Flask / FastAPI (Optional for API integration) |  
| **Database (Current)** | CSV (`blinkit.csv`) |  
| **Data Visualization** | Chart.js (for future improvements) |  

---

## **📂 Project Structure**  

```
fantastic4/
│── web_application/
    │── images/             # The graphs for the vizualisation 
    │── dashboad.html       # Main inventory dashboard
    │── start-audit.html    # Start inventory auditing page
    │── blinkit.csv         # Inventory dataset (CSV format)
    │── styles.css          # UI styling
    │── refresh_graphs.bat
│── README.md               # Project documentation
│── requirements.txt        # (Optional) Store images, icons, and assets
│── blinkit_dataset.csv             # The sample dataset
│── graph.py                # Generating graphs

```

---

## **🚀 How to Run the Project**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/PriyanshuKSharma/fantastic4.git
cd fantastic4
```

### **2️⃣ Open the Dashboard**  
- Open `dashboad.html` in your **web browser** or access it with
  ```bash
  https://PriyanshuKSharma.github.io/fantastic4/
  ```
- The dashboard allows you to **view inventory**, **start audits**, and **analyze stock levels**.  

### **3️⃣ Start an Audit**  
- Click **"Full Physical Inventory"** to go to the `start-audit.html` page.  
- This page loads inventory data from **blinkit.csv**.  
- The system processes and displays:  
  - **Product name, category, price, stock quantity, brand**  
  - **Sales volume, normalized demand, demand category, and inventory strategy**  

---

## **🔍 Detailed Explanation of Files**  

### **1️⃣ `dashboad.html` (Main Dashboard)**  
📌 The **dashboard page** provides an overview of inventory and includes:  
- **Warehouse selection** dropdown.  
- **Stock insights & visualizations** (to be added).  
- **Quick access** to inventory audits.  

### **2️⃣ `start-audit.html` (Audit Page)**  
📌 This page is responsible for **displaying inventory audit data**. It:  
- Loads data from **blinkit.csv**.  
- Displays stock details in **tabular format**.  
- Highlights **demand trends** based on sales volume.  
- Uses **fallback sample data** in case the CSV cannot be loaded directly (for browser security reasons).  

### **3️⃣ `blinkit.csv` (Inventory Dataset)**  
📌 Contains real inventory data, including:  
- **Product Name**  
- **Category** (Dairy, Household, Bakery, etc.)  
- **Price** (₹ value)  
- **Stock Quantity**  
- **Brand** (e.g., Amul, Colgate, Britannia)  
- **Sales Volume**  
- **Normalized Demand** (calculated based on highest sales volume)  
- **Demand Category** (Low, Medium, High)  
- **Inventory Strategy** (Storage recommendation)  

### **4️⃣ `styles.css` (UI & Styling)**  
📌 Manages the overall appearance of the dashboard and audit page. It:  
- Ensures a **modern, clean, and professional design**.  
- Includes **button styles, table formatting, and color schemes**.  
- Uses **FontAwesome icons** for a better user experience.  

---

## **💡 Future Improvements**  

🔹 **Add a Backend API** – Connect the system to a **Flask or FastAPI** backend for **database management**.  
🔹 **Store Inventory in a Database** – Use **PostgreSQL or Firebase** instead of a CSV file.  
🔹 **Real-Time Stock Updates** – Implement **WebSockets or Firebase Realtime Database**.  
🔹 **Graphical Insights** – Use **Chart.js or D3.js** to display trends visually.  
🔹 **Role-Based Access Control** – Differentiate access levels (Admin, Manager, Staff).  

---

## **🤝 Contributing**  
💡 If you’d like to improve this project, feel free to fork this repo, make changes, and submit a **pull request**!  

---

## **🔗 Contrbutors**  
If you have any questions or suggestions, feel free to reach out!  

📌 **GitHub:** [Rahul Kakkar](https://github.com/rahulkakkar01) <br>
📌 **GitHub:** [PriyanshuKSharma](https://github.com/PriyanshuKSharma) <br>
📌 **GitHub:** [Prajwal Ulli](https://github.com/PrajwalUlli)<br>
📌 **GitHub:** [Gaurav Salunke](https://github.com/Gaurav5442) <br>
📌 **GitHub:** [Aniruddha Deshmukh](https://github.com/ani9730)<br>
