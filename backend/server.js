import express from "express";
import fs from "fs";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const FILE = "./data/users.json";

/* SAFE READ FUNCTION */
const readData = () => {
  try {
    if (!fs.existsSync(FILE)) return [];

    const data = fs.readFileSync(FILE, "utf-8");

    if (!data) return [];

    return JSON.parse(data);
  } catch (err) {
    console.log("JSON Error fixed fallback:", err.message);
    return [];
  }
};

/* WRITE FUNCTION */
const writeData = (data) => {
  fs.writeFileSync(FILE, JSON.stringify(data, null, 2));
};

/* GET USERS */
app.get("/api/users", (req, res) => {
  const users = readData();
  res.json(users);
});

/* ADD USER */
app.post("/api/users", (req, res) => {
  const users = readData();

  const newUser = req.body;
  users.push(newUser);

  writeData(users);

  res.json({
    message: "User added successfully",
    users,
  });
});

app.listen(5000, () => {
  console.log("Server running on http://localhost:5000");
});