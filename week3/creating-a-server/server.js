const express = require("express");
const app = express();

// telling app to listen to port with callback function showing it is in fact working.
app.listen(3000, () => {
  console.log("App is listening on port 3000!");
});
