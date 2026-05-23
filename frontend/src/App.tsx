//Components
// import Header from "./components/Header";

// function App() {
//   return (
//     <div>
//       <head />
//       <p>Welcome to React App</p>
//     </div>
//   );
// }

// export default App;


// Props
// import UserCard from "./components/UserCard";

// function App() {
//   return (
//     <div>
//       <UserCard name="Rushi" role="Full Stack Developer" />
//       <UserCard name="John" role="Backend Developer" />
//     </div>
//   );
// }

// export default App;

// State
// import Counter from "./components/Counter";

// function App() {
//   return (
//     <div>
//       <Counter />
//     </div>
//   );
// }

// export default App;

// Component Composition
// import Card from "./components/Card";

// function App() {
//   return (
//     <Card>
//       <h2>Hello from inside Card</h2>
//       <p>This is composition pattern</p>
//     </Card>
//   );
// }

// export default App;


// import UserList from "./components/UserList";

// function App() {
//   const users = [
//     { id: 1, name: "Rushi" },
//     { id: 2, name: "Alex" },
//     { id: 3, name: "John" }
//   ];

//   return (
//     <UserList users={users} />
//   );
// }

// export default App;

// import Home from "./components/Home";

// export default function App() {
//   return <Home />;
// }

import { useEffect, useState } from "react";

export default function App() {
  const [name, setName] = useState("");
  const [users, setUsers] = useState([]);

  /* -------------------------
     FETCH USERS
  --------------------------*/
  const fetchUsers = async () => {
    const res = await fetch("http://localhost:5000/api/users");
    const data = await res.json();
    setUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  /* -------------------------
     ADD USER
  --------------------------*/
  const addUser = async () => {
    if (!name) return;

    await fetch("http://localhost:5000/api/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name }),
    });

    setName("");
    fetchUsers();
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>🚀 Fullstack Users App</h1>

      {/* FORM */}
      <input
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <button onClick={addUser}>Add User</button>

      {/* LIST */}
      <h2>Users</h2>

      {users.map((user, index) => (
        <p key={index}>👤 {user.name}</p>
      ))}
    </div>
  );
}