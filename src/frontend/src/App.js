import Home from "./components/Home";
import SelectedLayout from "./components/SelectedLayout";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/marathon/:year" element={<SelectedLayout />} />
            </Routes>
        </Router>
    );
}

export default App;
