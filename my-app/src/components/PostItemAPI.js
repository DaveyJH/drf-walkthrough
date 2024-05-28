import React from 'react';
import css from "./css/PostItem.module.css";

const PostItemAPI = (props) => {
  const { type, user, webformatURL, tags } = props.post;
  return (
    <div className={ css.SearchItem }>
      <p>Artwork type: { type }</p>
      <p>Artist: { user }</p>
      <img src={ webformatURL } />
      <p>Tags: { tags }</p>
    </div>
  )
}

export default PostItemAPI