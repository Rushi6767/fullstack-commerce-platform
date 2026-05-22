// import { useState } from "react";

// export default function ContactForm() {
//   // 1. STATE (form data)
//   const [form, setForm] = useState({
//     name: "",
//     email: "",
//   });

//   const [submitted, setSubmitted] = useState(null);

//   // 2. HANDLE INPUT CHANGE
//   const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
//     const { name, value } = e.target;

//     setForm((prev) => ({
//       ...prev,
//       [name]: value,
//     }));
//   };

//   // 3. HANDLE SUBMIT
//   const handleSubmit = (e: React.FormEvent) => {
//     e.preventDefault();

//     console.log("Form Data:", form);
//     setSubmitted(form);
//   };

//   return (
//     <div style={{ padding: "20px", maxWidth: "400px" }}>
//       <h2>Contact Form</h2>

//       <form onSubmit={handleSubmit}>
//         {/* NAME */}
//         <input
//           name="name"
//           placeholder="Name"
//           value={form.name}
//           onChange={handleChange}
//           style={{ display: "block", marginBottom: "10px" }}
//         />

//         {/* EMAIL */}
//         <input
//           name="email"
//           placeholder="Email"
//           value={form.email}
//           onChange={handleChange}
//           style={{ display: "block", marginBottom: "10px" }}
//         />

//         <button type="submit">Submit</button>
//       </form>

//       {/* OUTPUT */}
//       {submitted && (
//         <div style={{ marginTop: "20px" }}>
//           <h3>Submitted Data:</h3>
//           <pre>{JSON.stringify(submitted, null, 2)}</pre>
//         </div>
//       )}
//     </div>
//   );
// }


import { useState } from "react";

export default function ContactForm() {
  // -----------------------------
  // STATE MANAGEMENT
  // -----------------------------
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [errors, setErrors] = useState<any>({});
  const [submitted, setSubmitted] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);

  // -----------------------------
  // STYLES (INLINE DESIGN SYSTEM)
  // -----------------------------
  const styles = {
    page: {
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      background: "linear-gradient(135deg, #0f172a, #1e293b)",
      fontFamily: "Arial",
    },
    card: {
      width: "420px",
      padding: "30px",
      borderRadius: "16px",
      background: "#ffffff",
      boxShadow: "0 20px 50px rgba(0,0,0,0.3)",
    },
    title: {
      fontSize: "24px",
      fontWeight: "bold",
      marginBottom: "20px",
    },
    input: {
      width: "100%",
      padding: "12px",
      marginBottom: "10px",
      borderRadius: "8px",
      border: "1px solid #ddd",
      outline: "none",
    },
    textarea: {
      width: "100%",
      padding: "12px",
      height: "100px",
      borderRadius: "8px",
      border: "1px solid #ddd",
      marginBottom: "10px",
    },
    button: {
      width: "100%",
      padding: "12px",
      borderRadius: "8px",
      border: "none",
      background: loading ? "#94a3b8" : "#2563eb",
      color: "white",
      cursor: "pointer",
      fontWeight: "bold",
    },
    error: {
      color: "red",
      fontSize: "12px",
      marginBottom: "8px",
    },
    success: {
      background: "#dcfce7",
      padding: "10px",
      borderRadius: "8px",
      marginBottom: "10px",
      color: "#166534",
    },
  };

  // -----------------------------
  // INPUT HANDLER
  // -----------------------------
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // -----------------------------
  // VALIDATION
  // -----------------------------
  const validate = () => {
    let err: any = {};

    if (!form.name) err.name = "Name is required";
    if (!form.email.includes("@")) err.email = "Invalid email";
    if (form.message.length < 10)
      err.message = "Message must be at least 10 characters";

    return err;
  };

  // -----------------------------
  // SUBMIT HANDLER (FAKE API)
  // -----------------------------
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const validation = validate();
    setErrors(validation);

    if (Object.keys(validation).length > 0) return;

    setLoading(true);
    setSuccess(false);

    // fake API delay
    setTimeout(() => {
      setSubmitted(form);
      setLoading(false);
      setSuccess(true);

      setForm({
        name: "",
        email: "",
        message: "",
      });
    }, 1500);
  };

  // -----------------------------
  // UI
  // -----------------------------
  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h2 style={styles.title}>📩 Contact Us</h2>

        {success && (
          <div style={styles.success}>
            ✅ Message sent successfully!
          </div>
        )}

        {/* FORM */}
        <form onSubmit={handleSubmit}>
          {/* NAME */}
          <input
            name="name"
            placeholder="Your Name"
            value={form.name}
            onChange={handleChange}
            style={styles.input}
          />
          {errors.name && <div style={styles.error}>{errors.name}</div>}

          {/* EMAIL */}
          <input
            name="email"
            placeholder="Your Email"
            value={form.email}
            onChange={handleChange}
            style={styles.input}
          />
          {errors.email && <div style={styles.error}>{errors.email}</div>}

          {/* MESSAGE */}
          <textarea
            name="message"
            placeholder="Your Message..."
            value={form.message}
            onChange={handleChange}
            style={styles.textarea}
          />
          {errors.message && (
            <div style={styles.error}>{errors.message}</div>
          )}

          {/* BUTTON */}
          <button type="submit" style={styles.button} disabled={loading}>
            {loading ? "Sending..." : "Send Message 🚀"}
          </button>
        </form>

        {/* OUTPUT DEBUG (like dev tools) */}
        {submitted && (
          <div style={{ marginTop: "20px", fontSize: "12px" }}>
            <h4>Debug Output:</h4>
            <pre>{JSON.stringify(submitted, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  );
}