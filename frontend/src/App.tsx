//Components
// import Header from "./components/Header";

// function App() {
//   return (
//     <div>
//       <Header />
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



import { useState } from "react";

export default function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [count, setCount] = useState(0);
  const [task, setTask] = useState("");
  const [tasks, setTasks] = useState([]);

  // Add task
  const addTask = () => {
    if (!task.trim()) return;

    setTasks((prev) => [
      ...prev,
      { id: Date.now(), text: task, done: false },
    ]);

    setTask("");
  };

  // Toggle task done
  const toggleTask = (id) => {
    setTasks((prev) =>
      prev.map((t) =>
        t.id === id ? { ...t, done: !t.done } : t
      )
    );
  };

  // Delete task
  const deleteTask = (id) => {
    setTasks((prev) => prev.filter((t) => t.id !== id));
  };

  return (
    <div
      style={{
        fontFamily: "Arial",
        minHeight: "100vh",
        padding: "20px",
        background: darkMode ? "#0f172a" : "#f8fafc",
        color: darkMode ? "white" : "black",
        transition: "0.3s",
      }}
    >
      {/* HEADER */}
      <header
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "20px",
        }}
      >
        <h1>⚛️ React Power Dashboard</h1>

        <button
          onClick={() => setDarkMode(!darkMode)}
          style={{
            padding: "10px",
            cursor: "pointer",
          }}
        >
          Toggle {darkMode ? "Light" : "Dark"}
        </button>
      </header>

      {/* HERO SECTION */}
      <section
        style={{
          padding: "20px",
          borderRadius: "10px",
          background: darkMode ? "#1e293b" : "#ffffff",
          boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
          marginBottom: "20px",
        }}
      >
        <h2>Welcome Back 👋</h2>
        <p>This is a React single-component dashboard demo.</p>

        <button
          onClick={() => setCount(count + 1)}
          style={{
            padding: "10px 15px",
            marginTop: "10px",
            cursor: "pointer",
          }}
        >
          Click Counter: {count}
        </button>
      </section>

      {/* TASK INPUT */}
      <section
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        <input
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Add task..."
          style={{
            flex: 1,
            padding: "10px",
          }}
        />

        <button onClick={addTask}>Add</button>
      </section>

      {/* TASK LIST */}
      <section>
        <h3>Tasks ({tasks.length})</h3>

        {tasks.length === 0 && <p>No tasks yet 🚀</p>}

        {tasks.map((t) => (
          <div
            key={t.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              padding: "10px",
              marginBottom: "10px",
              borderRadius: "8px",
              background: darkMode ? "#334155" : "#e2e8f0",
              textDecoration: t.done ? "line-through" : "none",
            }}
          >
            <span onClick={() => toggleTask(t.id)} style={{ cursor: "pointer" }}>
              {t.text}
            </span>

            <button onClick={() => deleteTask(t.id)}>❌</button>
          </div>
        ))}
      </section>

      {/* FOOTER */}
      <footer
        style={{
          marginTop: "40px",
          textAlign: "center",
          opacity: 0.7,
        }}
      >
        Built with React ⚛️ | Single Component Power Demo
      </footer>
    </div>
  );
}