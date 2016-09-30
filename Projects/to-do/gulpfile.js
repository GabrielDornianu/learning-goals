var gulp = require('gulp');
    jade = require('gulp-jade');
    sass = require('gulp-sass');
    livereload = require('gulp-livereload');
    connect = require('gulp-connect');
    gulpIgnore = require('gulp-ignore');
 

SASS_FILES = './sass/**/*.sass'
JADE_FILES = './jade/**/*.jade'
JS_FILES = './js/**/*.js'

IGNORE_FILES = '**/_include/**/*'

APP_FILES = './app'

WATCH_FILES = [JADE_FILES, SASS_FILES, JS_FILES]

gulp.task('default', function () {
    // proprocess the sass and jade files
    gulp.start('sass', 'jade', 'js');
});

gulp.task('default:watch', function () {
    // watch all jade and sass files and compile them if they change
    gulp.watch(WATCH_FILES, ['default'])
});


gulp.task('sass', function () {
  return gulp.src(SASS_FILES)
    .pipe(gulpIgnore.exclude(IGNORE_FILES))
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(APP_FILES + "/css/"))
    .pipe(livereload());
});
 
gulp.task('jade', function() {
  return gulp.src(JADE_FILES)
    .pipe(gulpIgnore.exclude(IGNORE_FILES))
    .pipe(jade())
    .pipe(gulp.dest(APP_FILES))
    .pipe(livereload());
});


gulp.task('js', function(){
    return gulp.src(JS_FILES)
    .pipe(gulp.dest(APP_FILES + "/js/"))
    .pipe(livereload());
});

// Webserver
gulp.task('connect', function() {
  connect.server({
    root: APP_FILES,
    livereload: true
  });
});

// Develop
gulp.task('develop', function(){
    // start the webserver and livereload and 
    // start waching the sass and jade files
    livereload.listen();
    gulp.start('connect', 'default:watch');
})
