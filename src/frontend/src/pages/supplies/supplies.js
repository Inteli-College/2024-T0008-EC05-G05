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

  const openModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = true;
    setModalOpen(newModalOpen);
  };

  const closeModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = false;
    setModalOpen(newModalOpen);
  };

  const handleInputChange = (value, index) => {
    const newInputValues = [...inputValues];
    newInputValues[index] = value;
    setInputValues(newInputValues);
  };

  const handleDropdownChange = (event, index) => {
    const selected = event.target.value;
    setInputValues(prevInputValues => {
      const newInputValues = [...prevInputValues];
      newInputValues[index] = selected;
      return newInputValues;
    });
  };

  // Essa é a função que atualiza os dados para o backend 
  const sendValues = () => {
    console.log(inputValues);
    axios.put(`http://localhost:8000/posts/${selectedNumber}`, {
      nome_kit : 'Kit {selectedNumber}',
      id_kit : selectedNumber,
      item_1 : inputValues
    })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const fetchItems = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/posts/${selectedNumber}`);
      console.log(response.data.item_1); // Accessing item_1 directly
      // Update inputValues based on API response
      const newInputValues = [...inputValues];
      response.data.item_1.forEach((item, index) => {
        newInputValues[index] = item;
      });
      setInputValues(newInputValues);
      // Or if you want to open the modal for each item:
      response.data.item_1.forEach((item, index) => {
        openModal(index);
      });
    } catch (error) {
      console.log("error : ", error);
    }
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

