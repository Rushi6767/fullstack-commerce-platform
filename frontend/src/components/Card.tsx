// function Card({ children }) {
//   return (
//     <div style={{ border: "1px solid gray", padding: "10px" }}>
//       {children}
//     </div>
//   );
// }

// export default Card;

export default function Card({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "10px",
        minWidth: "120px",
        textAlign: "center",
      }}
    >
      {children}
    </div>
  );
}