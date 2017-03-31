import React from 'react';
export default class Submit extends React.Component {
    render() {
        return (
            <div className="submitPage row">
                <form onSubmit={this.handleSubmit} className="small-12 large-4 large-offset-4 columns">
                    <input type="text" ref="problemSN" placeholder="Enter problem ID"/>
                    <div className="inputGroup">
                        <legend>Language</legend>
                        <label htmlFor="languageC">
                            <input type="radio" name="language" value="c" id="languageC" required/>
                            C</label>
                        <label htmlFor="languageCpp">
                            <input type="radio" name="language" value="cpp" id="languageCpp"/>
                            C++</label>
                    </div>
                    <label htmlFor="exampleFileUpload" className="button expanded">Upload File</label>
                    <input type="file" id="exampleFileUpload" className="show-for-sr"/>
                </form>
            </div>
        );
    }
    handleSubmit(e) {
        return e.preventDefault();
    }
}
