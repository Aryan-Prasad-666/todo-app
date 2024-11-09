import React from 'react'

export default function Todocard(props) {
  return (
    <div className='todocard'>
        <h1>{props.name}</h1>
        <i class="fa-solid fa-pen-to-square"></i>
        <i class="fa-solid fa-trash"></i>
    </div>
  )
}
