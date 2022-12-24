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
    const [maleResults, setMaleResults] = useState([]);
    const [femaleResults, setFemaleResults] = useState([]);
    const [error, setError] = useState(null);
    const [femaleChartJson, setFemaleChartJson] = useState([]);
    const [maleChartJson, setMaleChartJson] = useState([]);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/results/" + marathon.year + "/M",
        })
            .then((response) => {
                setMaleResults(response.data);
                console.log(response.data);
                setMaleChartJson(
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
                console.log(maleChartJson);
                console.log(maleResults);
                setError(null);
            })
            .catch(setError);
    }, [marathon]);

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/api/results/" + marathon.year + "/F",
        })
            .then((response) => {
                setFemaleResults(response.data);
                console.log(response.data);
                setFemaleChartJson(
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
                console.log(femaleChartJson);
                console.log(femaleResults);
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
                    data: maleChartJson,
                    backgroundColor: ["skyblue"],
                    label: "Top Male Finish Times",
                },
                {
                    data: femaleChartJson,
                    backgroundColor: ["pink"],
                    label: "Top Female Finish Times",
                },
            ],
        });
        setHaveData(true);
    }, [
        marathon,
        femaleChartJson,
        femaleChartJson,
        maleChartJson,
        maleResults,
    ]);

    const options = {
        plugins: {
            title: {
                display: true,
                text: "Top Finish Times for Men and Women",
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
