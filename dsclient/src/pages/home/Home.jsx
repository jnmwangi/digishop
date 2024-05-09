import { useEffect } from "react"
import "./home.css"
import apiClient from "../../services/api-client"

export default function Home(){

    useEffect(()=>{
        apiClient.get('/api/products')
        .then(response=>{
            console.log(response.data)
        })
    }, [])

    return (<div className="banner">
        <h1>Digitized Shop</h1>
    </div>)
}