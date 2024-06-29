from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required=True)

videos={}

def abort_video_id_does_not_exist(video_id):
    if video_id not in videos:
        abort(404, message = 'video id does not exist')

def abort_video_id_exist(video_id):
    if video_id in videos:
        abort(409, message = 'video id already exists')



class Video(Resource):
    def get(self, video_id):
        abort_video_id_does_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self,video_id):
        abort_video_id_does_not_exist(video_id)
        del videos[video_id]
        return '',204



api.add_resource(Video, "/videos/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)