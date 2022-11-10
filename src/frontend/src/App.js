import Home from "./components/Home";
import MarathonView from "./components/MarathonView";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/marathon/:year" element={<MarathonView />} />
            </Routes>
        </Router>
    );
}

export default App;
