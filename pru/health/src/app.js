import React, { useState } from "react";

const BMIForm = () => {
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");
  const [bmi, setBmi] = useState(null);

  const calculateBMI = async () => {
    const res = await fetch("http://localhost:8000/bmi", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ weight: parseFloat(weight), height: parseFloat(height) }),
    });
    const data = await res.json();
    setBmi(data.bmi);
  };

  return (
    <div>
      <h2>Calculate BMI</h2>
      <input type="number" value={weight} onChange={(e) => setWeight(e.target.value)} placeholder="Weight (kg)" />
      <input type="number" value={height} onChange={(e) => setHeight(e.target.value)} placeholder="Height (cm)" />
      <button onClick={calculateBMI}>Submit</button>
      {bmi && <p>Your BMI: {bmi}</p>}
    </div>
  );
};

export default BMIForm;
