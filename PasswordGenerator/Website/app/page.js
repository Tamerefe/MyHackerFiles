"use client";

import { useState, useEffect } from "react";
import "./word.scss";

const PasswordGenerator = () => {
  const [characters, setCharacters] = useState("");
  const [digit, setDigit] = useState(15);
  const [password, setPassword] = useState("");
  const [securityLevel, setSecurityLevel] = useState("Nothing");
  const [progressWidth, setProgressWidth] = useState("1%");
  const [progressColor, setProgressColor] = useState("black");
  const [modalOpen, setModalOpen] = useState(false);
  
  const optionsSmall = "abcdefghijklmnopqrstuvwxyz".split("");
  const optionsBig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  const optionsNumber = "0123456789".split("");
  const optionsOther = "/#@&-_?=><!".split("");
  
  const optionsAll = [...optionsSmall, ...optionsBig, ...optionsNumber, ...optionsOther];

  const generatePassword = () => {
    let randomPassword = characters;
    let remainingLength = digit - characters.length;
    
    for (let i = 0; i < remainingLength; i++) {
      let randomIndex = Math.floor(Math.random() * optionsAll.length);
      randomPassword += optionsAll[randomIndex];
    }
    setPassword(randomPassword);
    updateSecurityLevel(remainingLength);
  };

  const updateSecurityLevel = (length) => {
    if (digit < 1) {
      setProgressWidth("1%");
      setProgressColor("black");
      setSecurityLevel("Nothing");
    } else if (digit < 4) {
      setProgressWidth("5%");
      setProgressColor("red");
      setSecurityLevel("Very Low");
    } else if (digit < 7) {
      setProgressWidth("35%");
      setProgressColor("hotpink");
      setSecurityLevel("Low");
    } else if (digit < 9) {
      setProgressWidth("55%");
      setProgressColor("yellow");
      setSecurityLevel("Standard");
    } else if (digit < 11) {
      setProgressWidth("75%");
      setProgressColor("turquoise");
      setSecurityLevel("Strong");
    } else {
      setProgressWidth("96%");
      setProgressColor("limegreen");
      setSecurityLevel("Very Strong");
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(password);
    alert("Password Copied!");
  };

  return (
    <div className="ml-5 mt-5 text-base">
      <h1 className="m-5 text-2xl font-bold">You're welcome Password Generator</h1>
      <p className="mt-5 ml-5">
        Would you like a word of your choice in your password? 
        <input className="ml-4 w-20 p-2 border-0 text-[#CCC] bg-white/10" type="text" value={characters} onChange={(e) => setCharacters(e.target.value)} placeholder="Dolliet" />
      </p>
      <p className="mt-5 ml-5">
        How many characters would you like in your password?
        <input className="ml-4 w-20 p-2 border-0 text-[#CCC] bg-white/10" type="number" value={digit} onChange={(e) => setDigit(Number(e.target.value))} placeholder="15" />
      </p>
      <p className="mt-5 ml-5" style={{ color: "crimson", fontSize: "12px" }}>Please don't let the word be greater than the character!</p>
      <div className="p-0.5 w-1/3 bg-white rounded-xl">
        <div className="bg-orange-600 w-0 h-3 rounded-xl" style={{ width: progressWidth, backgroundColor: progressColor }}></div>
      </div>
      <p className="mt-5 ml-5 text-[rgba(218,218,218,0.5)] text-sm" id="progressbarP">The security value of your password: {securityLevel}</p>
      <button className="m-5 p-2 text-base cursor-pointer" onClick={generatePassword}>Create</button>
      <button className="m-5 p-2 text-base cursor-pointer" onClick={copyToClipboard}>Copy to Clipboard</button>
      <button className="m-5 p-2 text-base cursor-pointer" onClick={() => setModalOpen(true)}>Info</button>
      {modalOpen && (
        <div className="modal" style={{ display: 'block' }}>
          <div className="modal-content">
            <div className="p-2 bg-[#092b37] text-white">
              <span className="close m-1" onClick={() => setModalOpen(false)}>&times;</span>
              <h2 className="m-3">What is Strong Password Generator?</h2>
            </div>
            <div className="pb-2">
              <p className="m-5">Strong password generator is an easy-to-use online password generator and automatic password generator that allows you to create passwords that are difficult to crack, and shows how strong the passwords you create are. Also, if you are wondering how secure my password is, you can find out how secure your password is with strong password generator.</p>
            </div>
          </div>
        </div>
      )}
      <p id="out">{password}</p>
    </div>
  );
};

export default PasswordGenerator;
