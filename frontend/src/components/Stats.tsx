import Card from "./Card";

const statsData = [
  { id: 1, label: "Users", value: "10K+" },
  { id: 2, label: "Projects", value: "250+" },
  { id: 3, label: "Performance", value: "99%" },
];

export default function Stats() {
  return (
    <section
      style={{
        display: "flex",
        justifyContent: "center",
        gap: "20px",
        padding: "40px",
      }}
    >
      {statsData.map((item) => (
        <Card key={item.id}>
          <h3>{item.value}</h3>
          <p>{item.label}</p>
        </Card>
      ))}
    </section>
  );
}