
import { useState } from "react";

const WaitTimeSearch = () => {
  const [treatment, setTreatment] = useState("");
  const [location, setLocation] = useState("");
  const [result, setResult] = useState(null);

  const search = async () => {
    const res = await fetch(`/api/waittimes?treatment=${treatment}&location=${location}`);
    const data = await res.json();
    setResult(data);
  };

  return (
    <div>
      <h2>Finn ventetid</h2>
      <input
        placeholder="Behandlingstype (f.eks. demens, hofte...)"
        onChange={(e) => setTreatment(e.target.value)}
      />
      <input
        placeholder="Sykehus (valgfritt)"
        onChange={(e) => setLocation(e.target.value)}
      />
      <button onClick={search}>Søk</button>
      {result && (
        <pre style={{ background: "#f0f0f0", padding: "1em" }}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
};

export default WaitTimeSearch;
