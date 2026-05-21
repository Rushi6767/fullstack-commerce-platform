export default function Header() {
  return (
    <header
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "15px 30px",
        borderBottom: "1px solid #ddd",
      }}
    >
      <h2>MyApp</h2>

      <nav style={{ display: "flex", gap: "15px" }}>
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">Contact</a>
      </nav>
    </header>
  );
}