import axios from "axios";

const apiClient = axios.create({
    baseURL:"http://localhost:5003"
});

export default apiClient;

