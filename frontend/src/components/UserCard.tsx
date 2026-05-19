// Props = data passed from parent → child

function UserCard(props) {
  return (
    <div style={{ border: "1px solid black", padding: "10px" }}>
      <h3>Name: {props.name}</h3>
      <p>Role: {props.role}</p>
    </div>
  );
}

export default UserCard;