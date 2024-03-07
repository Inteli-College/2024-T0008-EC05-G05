import React, { useState } from "react";
import ModalCreated from "../../components/Supplies_popup/supplie-popup.js";
import "./supplies.css";
import Sidebar from "../../components/Sidebar/Sidebar.js"; 

const Supplies = () => {
  // Variavel de estado para a sidebar
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Função para abrir e fechar a sidebar
  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  // Variavel de estado para o modal
  const [modalOpen, setModalOpen] = useState(Array(8).fill(false));

  // Abre o modal especifico para cada caixa
  const openModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = true;
    setModalOpen(newModalOpen);
  };

  // Fecha o modal especifico para cada caixa
  const closeModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = false;
    setModalOpen(newModalOpen);
  };

  return (
    <div className="Container">
    {/* Sidebar component */}
    <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />

    <div className="Row">
      {[0, 1, 2, 3].map((index) => (
        <div key={index} className="Item">
          <button onClick={() => openModal(index)}>Open Modal {index + 1}</button>
          <ModalCreated
            isOpen={openModal}
            onRequestClose={closeModal}
            className="modal"
            overlayClassName="overlay"
          ></ModalCreated>
        </div>
      ))}
    </div>
    <div className="Row">
      {[4, 5, 6, 7].map((index) => (
        <div key={index} className="Item">
          <button onClick={() => openModal(index)}>Open Modal {index + 1}</button>
          <ModalCreated
            isOpen={openModal}
            onRequestClose={closeModal}
            className="modal"
            overlayClassName="overlay"
          ></ModalCreated>
        </div>
      ))}
    </div>
  </div>
);
};


export default Supplies;
