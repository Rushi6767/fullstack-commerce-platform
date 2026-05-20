function UserList({ users }) {
  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>
          <h4>{user.name}</h4>
        </div>
      ))}
    </div>
  );
}

export default UserList;