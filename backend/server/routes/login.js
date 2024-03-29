const express = require("express");
const Users = require("../models/userModel");

const router = express.Router();

router.get("/", (req, res) => {
  res.status(200).json({ message: "Welcome to Login Endpoint" });
});

router.post("/", async (req, res) => {
  const { email, password } = req.body;
  try{
  const user = await Users.findOne({ email, password });
  if (user) {
    res.status(200).json({ message: "Login Successful" , success: true ,data:{uid:user._id} });
  }
  else{
      res.status(401).json({ message: "Invalid Credentials",success:false });
  }}catch(e){
    res.status(500).json({ message: e.message});
  }
});

module.exports = router;
