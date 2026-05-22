import Header from "../components/Header";
import Hero from "../components/Hero";
import Stats from "../components/Stats";
import ContactForm from "../components/form/ContactForm";

export default function Home() {
  return (
    <div>
      <Header />
      <Hero />
      <Stats />
      <ContactForm />
    </div>
  );
}