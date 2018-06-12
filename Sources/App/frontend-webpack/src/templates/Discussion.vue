<template>
    <div>
        <nav-bar></nav-bar>
        <div class="comments">
            <div class="comment-wrap">
                <div class="photo">
                    <div class="avatar"
                         style="background-image: url('https://s3.amazonaws.com/uifaces/faces/twitter/dancounsell/128.jpg')"></div>
                </div>
                <div class="comment-block">
                    <form action="">
                        <textarea name="" id="" class="comment-textarea" cols="30" rows="3"
                                  placeholder="Add comment..."></textarea>
                    </form>
                </div>

            </div>
            <div class="comment-wrap" style="height: 40px;">
                <button class="btn-primary float-right"
                        style="border-radius: 5px; padding-left: 20px; padding-right: 20px;">Post
                </button>
            </div>
            <div class="comment-wrap">
                <div class="photo">
                    <div class="avatar"
                         style="background-image: url('https://s3.amazonaws.com/uifaces/faces/twitter/jsa/128.jpg')"></div>
                </div>
                <div class="comment-block">
                    <p class="comment-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto temporibus
                        iste nostrum dolorem natus recusandae incidunt voluptatum. Eligendi voluptatum ducimus
                        architecto tempore, quaerat explicabo veniam fuga corporis totam reprehenderit quasi
                        sapiente modi tempora at perspiciatis mollitia, dolores voluptate. Cumque, corrupti?</p>
                    <div class="bottom-comment">
                        <div class="comment-date">Aug 24, 2014 @ 2:35 PM</div>
                        <ul class="comment-actions">
                            <li class="complain">Complain</li>
                            <li class="reply">Reply</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue';

    export default {
        components: {
            'nav-bar': NavBar,
        },
    }
</script>

<style scoped>
    .comment-textarea {
        outline: none;
        border: none;
        display: block;
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
        font-size: 1rem;
        color: #555f77;
    }

    .comment-textarea::placeholder {
        color: #ced2db;
    }

    p {
        line-height: 1.3125rem;
    }

    .comments {
        margin: 2.5rem auto 0;
        max-width: 40rem;
        padding: 0 1.25rem;
    }

    .comment-wrap {
        margin-bottom: 1.25rem;
        display: table;
        width: 100%;
        min-height: 5.3125rem;
    }

    .photo {
        padding-top: 0.625rem;
        display: table-cell;
        width: 3.5rem;
    }

    .photo .avatar {
        height: 2.25rem;
        width: 2.25rem;
        border-radius: 50%;
        background-size: contain;
    }

    .comment-block {
        padding: 1rem;
        background-color: #fff;
        display: table-cell;
        vertical-align: top;
        border-radius: 0.1875rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.08);
    }

    .comment-block textarea {
        width: 100%;
        resize: none;
    }

    .comment-text {
        color: #555f77 !important;
        margin-bottom: 1.25rem;
    }

    .bottom-comment {
        color: #acb4c2;
        font-size: 0.875rem;
    }

    .comment-date {
        float: left;
    }

    .comment-actions {
        float: right;
        margin-bottom: 0;
    }

    .comment-actions li {
        display: inline;
        margin: -2px;
        cursor: pointer;
    }

    .comment-actions li.complain {
        padding-right: 0.75rem;
        border-right: 1px solid #e1e5eb;
    }

    .comment-actions li.reply {
        padding-left: 0.75rem;
        padding-right: 0.125rem;
    }

    .comment-actions li:hover {
        color: #0095ff;
    }
</style>