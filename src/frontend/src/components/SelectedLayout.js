import Header from "./Header";
import Sidebar from "./Sidebar";
import FilterNavbar from "./FilterNavbar";
import MarathonView from "./MarathonView";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

function SelectedLayout(props) {
    const location = useLocation();
    const marathon = location.state?.marathon;

    const [selected, setSelected] = useState(1);

    useEffect(() => {
        setSelected(1);
    }, [marathon]);

    return (
        <div className="App">
            <Sidebar></Sidebar>
            <Header marathon={marathon}></Header>
            <FilterNavbar
                selected={selected}
                setSelected={setSelected}
            ></FilterNavbar>
            <MarathonView
                marathon={marathon}
                selected={selected}
            ></MarathonView>
        </div>
    );
}
export default SelectedLayout;
