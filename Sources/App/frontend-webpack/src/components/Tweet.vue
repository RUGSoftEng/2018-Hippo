<template lang="html">
    <div class=tweet>
        <div class="row">
            <div class="col-1">
                <img src="{{tweetData.user_profile_image}}" style="height: 40px; border-radius: 50%;">
            </div>
            <div class="col-11" style="padding-left: 20px;">
                <div style="">
                    <h4 style="margin-top: 5px;">{{tweetData.user_name}}<a href="https://twitter.com/statuses/{{tweetData.id}}"><img src="../assets/icons8-external-link.svg" style="width: 18px; margin-left: 20px;"></a></h4>
                </div>
                <div style="">
                    {{tweetData.content}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['tweetData'],

    }
</script>

<style scoped lang="css">
    .tweet {
        display: inline-block;
        color: black;
        font-size: 16px;
        line-height: 24px;
        border-radius: 5px;
        border: 1px solid #A7A7A7;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
        margin: 10px 5px;
        padding: 16px 16px 16px 16px;
        width: 600px;
        background-color: white;
    }

    .tweet p {
        font-size: 16px;
        font-weight: normal;
        line-height: 20px;
    }

    .tweet a {
        color: inherit;
        font-weight: normal;
        text-decoration: none;
        outline: 0 none;
    }

    .tweet a:hover,
    .tweet a:focus {
        text-decoration: underline;
    }
</style>
