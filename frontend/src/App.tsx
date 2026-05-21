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

import Home from "./components/Home";

export default function App() {
  return <Home />;
}