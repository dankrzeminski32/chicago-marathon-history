import { useState, useEffect } from "react";
import axios from "axios";

function Sidebar() {
    const [marathons, setMarathons] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/marathons/",
        })
            .then((response) => {
                console.log(response.data);
                setMarathons(response.data);
                setError(null);
            })
            .catch(setError);
    }, []);

    if (error) return <p>an error occured</p>;

    return (
        <div id="sidebar-wrapper">
            <ul className="sidebar-nav">
                <li className="sidebar-brand">
                    <a href="#">Years</a>
                </li>
                {marathons.map(({ id, year }) => {
                    return (
                        <li key={id} className="sidebar-brand">
                            <a href="#">{year}</a>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default Sidebar;
