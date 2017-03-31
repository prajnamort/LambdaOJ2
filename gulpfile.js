var gulp = require('gulp');
var del = require('del');

var conf = {
    js: "fe/public/**/*.js",
    html: "fe/public/**/*.html",
    dest: "main/static/",
    desthtml: "main/templates/main/",
    destindex: "main/templates/main/index.html"
};

gulp.task('copy:js', function(){
    gulp.src(conf.js).pipe(gulp.dest(conf.dest));
});

gulp.task('copy:html', function(){
    gulp.src(conf.html).pipe(gulp.dest(conf.desthtml));
});

gulp.task('copy', ['copy:js', 'copy:html']);

gulp.task('clean', function(){
    del(conf.dest);
    del(conf.destindex);
})

gulp.task('default', ['clean', 'copy']);
