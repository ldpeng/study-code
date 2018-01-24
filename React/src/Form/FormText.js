import React from 'react';

export default class FormText extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isGoing: true,
            numberOfGuests: "",
            favorite: "",
            remark: ""
        };

        this.handleInputChange = this.handleInputChange.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            //ES6语法
            [name]: value
        });
    }

    render() {
        //受控组件：表单控件需要通过value或者checked属性及事件触发的方式让React去重新渲染
        return (
            <form>
                <label>
                    Is going:
                    <input
                        name="isGoing"
                        type="checkbox"
                        checked={this.state.isGoing}
                        onChange={this.handleInputChange}/>
                </label>
                <br/>
                <label>
                    Number of guests:
                    <input
                        name="numberOfGuests"
                        type="text"
                        value={this.state.numberOfGuests}
                        onChange={this.handleInputChange}/>
                </label>
                <br/>
                <label>
                    Pick your favorite La Croix flavor:
                    <select name="favorite" value={this.state.favorite} onChange={this.handleInputChange}>
                        <option value="grapefruit">Grapefruit</option>
                        <option value="lime">Lime</option>
                        <option value="coconut">Coconut</option>
                        <option value="mango">Mango</option>
                    </select>
                </label>
                <br/>
                <label>
                    Remark:
                    <textarea name="remark" value={this.state.value} onChange={this.handleInputChange}/>
                </label>
            </form>
        );
    }
}