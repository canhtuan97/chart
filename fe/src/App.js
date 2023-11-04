import logo from "./logo.svg";
import { Line } from "react-chartjs-2";
import Chart from "chart.js/auto";
import "./App.css";
import faker from "faker";
import React, { useState, useEffect } from "react";

import axios from "axios";

const options = {
  responsive: true,
  interaction: {
    mode: "index",
    intersect: false,
  },
  stacked: false,
  plugins: {
    title: {
      display: true,
      text: "Chart.js Line Chart - Multi Axis",
    },
  },
  scales: {
    y: {
      type: "linear",
      display: true,
      position: "left",

      y1: {
        type: "linear",
        display: true,
        position: "right",
        grid: {
          drawOnChartArea: false,
        },
      },
    },
  },
};

const labels = ["January", "February", "March", "April", "May", "June", "July"];

function App() {
  const [data, setData] = useState();

  const getData = async () => {
    const dataChart = await axios.request({
      method: "get",
      maxBodyLength: Infinity,
      url: "http://127.0.0.1:9000/data",
      headers: {},
    });

    if (dataChart.status !== 500) {
      setData({
        labels: dataChart.data.Date.map((value) => new Date(value)),
        datasets: [
          {
            label: "Dataset 2",
            data: dataChart.data.Price,
            borderColor: "rgb(53, 162, 235)",
            backgroundColor: "rgba(53, 162, 235, 0.5)",
            yAxisID: "y1",
          },
        ],
      });
    }
  };
  useEffect(() => {
    getData();
  }, []);

  // const interval = setInterval(() => {
  //   console.log("Fetching data...");
  //   getData();
  // }, 5000);

  return (
    <div>
      <div>ca</div>
      {data && (
        <div>
          <Line options={options} data={data} />
        </div>
      )}
    </div>
  );
}

export default App;
