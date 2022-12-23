import { useEffect, useState } from "react";
import React from "react";
import {
    Chart,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend,
} from "chart.js";
import { Scatter } from "react-chartjs-2";
import axios from "axios";

export const LineFinishTimes = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [haveData, setHaveData] = useState(false);
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);
    const [chartJson, setChartJson] = useState([]);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/results/" + marathon.year,
        })
            .then((response) => {
                setResults(response.data);
                console.log(response.data);
                setChartJson(
                    response.data.map((item) => {
                        const container = {};
                        container["x"] = item.place_overall;
                        var hoursMinutes = item.finish_time.split(/[.:]/);
                        var hours = parseInt(hoursMinutes[0], 10);
                        var minutes = hoursMinutes[1]
                            ? parseInt(hoursMinutes[1], 10)
                            : 0;
                        var finish_time_as_number = hours + minutes / 60;
                        container["y"] = finish_time_as_number;
                        return container;
                    })
                );
                console.log(chartJson);
                console.log(results);
                setError(null);
            })
            .catch(setError);
    }, [marathon]);

    Chart.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

    useEffect(() => {
        SetChartData({
            labels: "A dataset",
            datasets: [
                {
                    data: chartJson,
                    backgroundColor: ["skyblue", "pink"],
                },
            ],
        });
        setHaveData(true);
    }, [marathon, chartJson, results]);

    const options = {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    };

    if (!haveData || error) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Scatter options={options} data={chartData} />
        </div>
    );
};
