import React, { useState } from "react";
import ModalCreated from "../../components/Supplies_popup/supplie-popup.js";
import "./supplies.css";
import Sidebar from "../../components/Sidebar/Sidebar.js";
import axios from "axios";

const Supplies = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [selectedNumber, setSelectedNumber] = useState(null); // State to hold selected number
  const [kitData, setKitData] = useState(Array(8).fill({ hasMedicine: false, quantity: 0 }));

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  const handleSaveKit = () => {
    const kitDataToSend = kitData.map(({ hasMedicine, quantity }) => ({ hasMedicine, quantity }));
    // You can send kitDataToSend to backend using axios here
    console.log("Kit Data to Send:", kitDataToSend);
  };

  const options = [
    "Curativo adesivo",
    "Agulha",
    "Ampola Lidocaína",
    "Luva de cirurgia",
    "Gaze estéril",
    "Antisséptico",
    "Seringa descartável",
    "Máscara N95",
  ];

  return (
    <div className="Container">
      <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
      <div className="Header">
        <p>Escolha um kit</p>
        <select
          value={selectedNumber}
          onChange={(event) => setSelectedNumber(event.target.value)}
        >
          <option value="">Escolha um kit</option>
          {[1, 2, 3, 4, 5].map((number) => (
            <option key={number} value={number}>
              {number}
            </option>
          ))}
        </select>
      </div>
      <div className="Row">
        {options.map((option, index) => (
          <div key={index} className="Item">
            <div className="ButtonContainer">
              <button id="home_button"></button>
            </div>
            <ModalCreated
              key={index}
              isOpen={true}
              onRequestClose={() => {}}
              title={option}
              hasMedicine={kitData[index].hasMedicine}
              quantity={kitData[index].quantity}
              onToggleMedicine={() => {
                const updatedKitData = [...kitData];
                updatedKitData[index].hasMedicine = !kitData[index].hasMedicine;
                setKitData(updatedKitData);
              }}
              onIncrementQuantity={() => {
                const updatedKitData = [...kitData];
                updatedKitData[index].quantity++;
                setKitData(updatedKitData);
              }}
              onDecrementQuantity={() => {
                const updatedKitData = [...kitData];
                if (updatedKitData[index].quantity > 0) {
                  updatedKitData[index].quantity--;
                }
                setKitData(updatedKitData);
              }}
            />
          </div>
        ))}
      </div>
      <div>
        <button onClick={handleSaveKit}>Salvar Kit</button>
      </div>
    </div>
  );
};

export default Supplies;

