import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function Sidebar({
    onHide,
    marathonStateChanger,
    isSidebarVisibleOnSmallScreen,
}) {
    const [marathons, setMarathons] = useState([]);
    const [error, setError] = useState(null);
    const [selectedYear, setSelectedYear] = useState(null);

    const handleClick = (event) => {
        if (event.target.classList.contains("sidebar-item")) {
            var sidebarItemsLinks =
                document.getElementsByClassName("sidebar-item");
            console.log(sidebarItemsLinks);
            for (var j = 0; j < sidebarItemsLinks.length; j++) {
                sidebarItemsLinks[j].style.backgroundColor = "";
            }
            event.target.style.backgroundColor = "#585858";
        }
    };

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/marathons/",
        })
            .then((response) => {
                setMarathons(response.data);
                setError(null);
            })
            .catch(setError);
    }, []);

    if (error) return <p>an error occured</p>;

    return (
        <div
            id="sidebar-wrapper"
            className={
                isSidebarVisibleOnSmallScreen ? "d-block" : "d-none d-md-block"
            }
        >
            <ul
                className={`sidebar-nav ${
                    isSidebarVisibleOnSmallScreen
                        ? "d-block"
                        : "d-none d-md-block"
                }`}
            >
                <li className="sidebar-brand">
                    <Link to="/">Years</Link>
                </li>
                {marathons.map((marathon) => {
                    return (
                        <li
                            key={marathon.id}
                            className="sidebar-brand"
                            onClick={handleClick}
                        >
                            <Link
                                onClick={() => {
                                    onHide();
                                    marathonStateChanger(marathon);
                                }}
                                className="sidebar-item"
                                to="/"
                            >
                                {marathon.year}
                            </Link>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default Sidebar;
