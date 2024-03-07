import { useState } from "react";
import ModalCreated from "../../components/Supplies_popup/supplie-popup.js";

const Supplies = () => {
  const [isOpen, setIsOpen] = useState(false);

  function openModal() {
    setIsOpen(true);
  }

  function closeModal() {
    setIsOpen(false);
  }

  return (
    <div className="Container">
        <ModalCreated
                isOpen={isOpen}
                onRequestClose={closeModal}
                className="modal"
                overlayClassName="overlay"></ModalCreated>
    </div>
  );
}

export default Supplies;
