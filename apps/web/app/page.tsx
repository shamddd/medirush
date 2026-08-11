export default function Home() {
  return (
    <main className="page">
      <section className="hero">
        <span className="eyebrow">MediRush</span>

        <h1>Medicines from pharmacies around you.</h1>

        <p>
          Search medicines, upload prescriptions, compare nearby pharmacies,
          and track your delivery.
        </p>

        <div className="actions">
          <button className="primary">Find Medicines</button>
          <button className="secondary">Upload Prescription</button>
        </div>
      </section>
    </main>
  );
}