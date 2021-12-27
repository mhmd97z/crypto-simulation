pragma solidity ^0.5.10;

contract CustomERC20 {
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    mapping (address => mapping(address => uint256)) private _allowancesExpireTime;

    uint256 private _totalSupply;

    event Transfer(address sender, address recipient, uint256 amount);
    event Approval(address owner, address spender, uint256 amount);
    event TimeApproval(address owner, address spender, uint256 expireTime);
    event Paused(address account);
    event Unpaused(address account);

    bool private _paused;
    address private _pauser;

    constructor () internal {
        // TODO
        _paused = false;
        _pauser = msg.sender;
    }

    modifier whenNotPaused() {
        // TODO
        require(_paused == false);
        _;
    }

    /**
     * @dev Only Puaser.
     *
     * Checks whether msg.sender is pauser or not
     */
    modifier onlyPauser() {
        // TODO
        require(msg.sender == _pauser);
        _;
    }

    /**
     * @dev Pause.
     *
     * Get contract pause status
     */
    function paused() public view returns (bool) {
        return _paused;
    }

    /**
     * @dev isPauser.
     *
     * Checks whether account is pauser or not
     */
    function isPauser(address account) private view returns (bool) {
        // TODO
        if(account == _pauser){
            return true;
        }
        else{
            return false;
        }
    }

    /**
     * @dev Pause.
     *
     * Pauses contract all external and public functions
     *
     * Requirements:
     *
     * - the caller must be the pauser
     */
    function pause() public onlyPauser returns (bool) {
        // TODO
        _paused = true;
        emit Paused(msg.sender);
        return true;
    }

    /**
     * @dev Pause.
     *
     * Unpauses contract all external and publuic functions
     *
     * Requirements:
     *
     * - the caller must be the pauser
     */
    function unpause() public onlyPauser {
        // TODO
        _paused = false;
        emit Unpaused(msg.sender);
    }

    /**
     * @dev Returns the amount of tokens in existence.
     */
    function totalSupply() public view returns (uint256) {
        // TODO
        return _totalSupply;
    }

     /**
     * @dev Returns the amount of tokens owned by `account`.
     */
    function balanceOf(address account) public view returns (uint256) {
        // TODO
        return _balances[account];
    }

    /**
     * @dev {ERC20-transfer}.
     *
     * Requirements:
     *
     * - `recipient` cannot be the zero address.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address recipient, uint256 amount) public whenNotPaused returns (bool) {
        // TODO
        require(recipient != address(0));
        require(_balances[msg.sender] >= amount);
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev {ERC20-allowance}.
     */
    function allowance(address owner, address spender) public view whenNotPaused returns (uint256) {
        // TODO
        return _allowances[owner][spender];
    }

    /**
     * @dev {ERC20-approve}.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     */
    function approve(address spender, uint256 amount, uint expireTime) public whenNotPaused returns (bool) {
        // TODO
        require(spender != address(0));
        _approve(msg.sender, spender, amount);
        _approveExpireTime(msg.sender, spender, expireTime);
        return true;
    }

    /**
     * @dev {ERC20-transferFrom}.
     *
     * Emits an {Approval} event indicating the updated allowance. This is not
     * required by the EIP. See the note at the beginning of {ERC20};
     *
     * Requirements:
     * - `sender` and `recipient` cannot be the zero address.
     * - `sender` must have a balance of at least `amount`.
     * - the caller must have allowance for `sender`'s tokens of at least
     * `amount`.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public whenNotPaused returns (bool) {
        // TODO
        require(now >= _allowancesExpireTime[sender][msg.sender]);
        require(amount >= _allowances[sender][msg.sender]);
        require(amount >= _balances[sender]);
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Moves tokens `amount` from `sender` to `recipient`.
     *
     * This is internal function is equivalent to {transfer}, and can be used to
     * e.g. implement automatic token fees, slashing mechanisms, etc.
     *
     * Emits a {Transfer} event.
     *
     * Requirements:
     *
     * - `sender` cannot be the zero address.
     * - `recipient` cannot be the zero address.
     * - `sender` must have a balance of at least `amount`.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        // TODO
        _balances[sender] = _balances[sender]-amount;
        _balances[recipient] = _balances[recipient]+amount;
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Destroys `amount` tokens from `account`, reducing the
     * total supply.
     *
     * Emits a {Transfer} event with `to` set to the zero address.
     *
     * Requirements
     *
     * - `account` cannot be the zero address.
     * - `account` must have at least `amount` tokens.
     */
    function _burn(address account, uint256 amount) internal {
        // TODO
        require(account != address(0));
        require(_balances[account] >= amount);
        _balances[account] = _balances[account] - amount;
        _totalSupply = _totalSupply - amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Sets `amount` as the allowance of `spender` over the `owner`s tokens.
     *
     * This is internal function is equivalent to `approve`, and can be used to
     * e.g. set automatic allowances for certain subsystems, etc.
     *
     * Emits an {Approval} event.
     *
     * Requirements:
     *
     * - `owner` cannot be the zero address.
     * - `spender` cannot be the zero address.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        // TODO
        require(spender != address(0));
        require(owner != address(0));
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Sets `expire time` as the allowance of `spender` over the `owner`s tokens.
     *
     * Emits an {TimeApproval} event.
     *
     * Requirements:
     *
     * - `owner` cannot be the zero address.
     * - `spender` cannot be the zero address.
     */
    function _approveExpireTime(address owner, address spender, uint expireTime) internal {
        // TODO
        require(owner != address(0));
        _allowancesExpireTime[owner][spender] = expireTime;
        emit TimeApproval(owner, spender, expireTime);
    }

    /** @dev Creates `amount` tokens and assigns them to `account`, increasing
     * the total supply.
     *
     * Emits a {Transfer} event with `from` set to the zero address.
     *
     * Requirements
     *
     * - `to` cannot be the zero address.
     */
    function _mint(address account, uint256 amount) internal {
        //TODO
        require(account != address(0));
        
        _totalSupply = _totalSupply + amount;
        _balances[account] = _balances[account] + amount;
        emit Transfer(address(0), account, amount);
    }
    
    /**
     * @dev Destroys `amount` tokens from `account`.`amount` is then deducted
     * from the caller's allowance.
     *
     * See {_burn} and {_approve}.
     */
    function _burnFrom(address account, uint256 amount) internal {
        // TODO
        require(_allowances[account][msg.sender] >= amount);
        require(_allowancesExpireTime[account][msg.sender] >= now);
        _burn(account, amount);
        _approve(account, msg.sender, _allowances[account][msg.sender] - amount);
    }
}
