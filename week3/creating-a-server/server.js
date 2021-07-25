const express = require("express");
const app = express();

// telling app to listen to port with callback function showing it is in fact working.
app.listen(6000, () => {
  console.log("App is listening on port 6000!");
});
// using 6000 rather than 3000 because I have 3000 already in use on my machine and can't find where that 
// server is running