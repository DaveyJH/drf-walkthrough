import React from 'react';
import css from "./css/PostItem.module.css";

const PostItem = (props) => {
  const { title, name, image, description, paragraph } = props.post;
  return (
    <div className={ css.SearchItem }>
      <p>Title: { title }</p>
      <p>Artist: { name }</p>
      <img src={ image } alt={ paragraph } />
      <p>Description: { description }</p>
    </div>
  )
}

export default PostItem